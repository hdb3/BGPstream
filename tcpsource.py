# tcpsource.py
# refer to tcpsource.txt for details

SOCKET_RETRY_LIMIT = 999

import errno
import os
import sys
import socket

from logger import trace, info, show, warn, error
from basemessage import ByteStream
import source

class Source(source.Source):

    def __init__(self,address,**kargs):
        self.address = address
        if 'passive' in kargs:
            passive = bool(kargs['passive'])
        else:
            passive = True

        if 'active' in kargs:
            active = bool(kargs['active'])
        else:
            active = False

        assert active != passive
        self.passive = passive

        if 'bufsiz' in kargs:
            self.bufsiz = kargs['bufsiz']
        else:
            self.bufsiz = 4096
        self.output_type = ByteStream
        source.Source.__init__(self)
    
    def __iter__(self):
        if self.passive:
            self._passive_init()
        else:
            self._active_init()
        return self

    def __next__(self):
        try:
            buf = self.sock.recv(self.bufsiz)
            if buf:
                return self.sock.recv(self.bufsiz)
            else:
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
        error("NOT IMPLEMENTED YET")
        exit()


    def _passive_init(self):

        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # attempt to bind socket to listen address

        info("binding socket to %s\n" % str(self.address))
        bound = False
        for i in range(SOCKET_RETRY_LIMIT):
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
                    sleep(3)
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
