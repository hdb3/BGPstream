# tcpsource.py
# refer to tcpsource.txt for details

import errno
import os
import sys
import socket

from logger import trace, info, show, warn, error
from basemessage import WireMessage
import source

class Source(source.Source):

    #def __init__(self,address,active=True,passive=False,bufsiz=4096):
    def __init__(self,address,**kargs):
        if 'passive' in kargs:
            self.passive = bool(kargs['passive'])

        assert active != passive
        self.passive = passive
        self.output_type = WireMessage
        self.bufsiz = bufsiz
        source.Source.__init__(self)
    
    def __iter__(self):
        if self.passive:
            self._passive_init()
        else:
            self._active_init()
        return self

    def __next__(self):
        try:
            return self.sock.recv(BUFSIZ)

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
                error("unrecoverable error %s" % e + " connecting to %s\n" % _name(self.address))
                break
            except Exception as e:
                error(("unknown error %s" % e) + (" connecting to %s\n" % _name(self.address)))
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
            info("connected to %s\n" % _name(self.remote_address))
            return
        except (socket.herror,socket.gaierror) as e:
            error("unrecoverable error %s" % e + " connecting to %s\n" % _name(self.address))
            exit()
        except Exception as e:
            error(("unknown error %s" % e) + (" connecting to %s\n" % _name(self.address)))
            exit()
