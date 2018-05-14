# tcpsocket.py

CONNECT_RETRY_LIMIT = 999
CONNECT_RETRY_DELAY = 10

import errno
import os
import sys
import socket
from time import sleep

from logger import *
from basemessage import ByteStream

class Socket:

    def __init__(self,address,passive):

        self.address = address
        # self.passive = passive
    
        if passive:
            self._passive_init()
        else:
            self._active_init()

    def send(self,msg):
        try:
            self.sock.sendall(msg)
        except socket.error as errmsg:
            error("socket.error %s" % errmsg)

    def recv(self,bufsiz):
        trace()
        try:
            buf = self.sock.recv(bufsiz)
            if buf:
                return buf
            else:
                trace("exiting")
                pass
                # fall through to exit because the receive zero length indicates a closing connection

        except socket.timeout:
            self.sock.close()
            self.sock.shutdown(socket.SHUT_RDWR)
            error("\nwaited too long on recv %s\n")
        except socket.error as errmsg:
                error("\nunexpected error on recv %s\n" % errmsg)
        except Exception as e:
            error("\nunknown error on recv %s\n" % e)

        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
        except Exception as e:
            ("ignored exception closing listen socket: %s\n" % str(e))
        raise StopIteration

    def _active_init(self):
        for n in range(CONNECT_RETRY_LIMIT):
            try:
                info("attempting connection to %s\n" % str(self.address))
                self.sock = socket.create_connection(self.address,1)
                self.remote_address = self.sock.getpeername()
                self.sock.setblocking(True)
                info("connected to %s\n" % str(self.address))
                return

            except (socket.error,socket.timeout) as e:
                self.last_socket_error = e
                sleep(CONNECT_RETRY_DELAY)
                continue
            except (socket.herror,socket.gaierror) as e:
                error("unrecoverable error %s" % e + " connecting to %s\n" % str(self.address))
                break
            except Exception as e:
                error("unknown error %s" % e + " connecting to %s\n" % str(self.address))
                break

        raise StopIteration


    def _passive_init(self):

        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # attempt to bind socket to listen address

        info("binding socket to %s\n" % str(self.address))
        bound = False
        for i in range(CONNECT_RETRY_LIMIT):
            try:
                self.listen_sock.bind(self.address)
                bound = True
                break
            except OSError as e:
                if e.errno != errno.EADDRINUSE:
                    error("%s" % os.strerror(e.errno))
                    break
                else:
                    info("bind - address in use - will wait and try again")
                    sleep(CONNECT_RETRY_DELAY)
            except (socket.herror,socket.gaierror) as e:
                error("unrecoverable error %s" % e + " connecting to %s\n" % str(self.address))
                break
            except Exception as e:
                error(("unknown error %s" % e) + (" connecting to %s\n" % str(self.address)))
                break

        if bound:
            info("bind success")
        else:
            error("bind failure")
            exit()

    # wait for incoming connection on listen address

        info("awaiting connection on %s\n" % str(self.address))
        self.listen_sock.listen(0)

        try:
            self.sock,self.remote_address = self.listen_sock.accept()
            self.sock.setblocking(True)
            info("connected to %s\n" % str(self.remote_address))
            return
        except (socket.herror,socket.gaierror) as e:
            error("unrecoverable error %s" % e + " connecting to %s\n" % str(self.address))
            exit()
        except Exception as e:
            error(("unknown error %s" % e) + (" connecting to %s\n" % str(self.address)))
            exit()
