import logging

from sleekxmpp import ClientXMPP

logger = logging.getLogger(__name__)

class Bot(ClientXMPP):
    def __init__(self, jid, password, room, nick, **kwargs):
        super(Bot, self).__init__(jid, password)

        self.jid = jid
        self.password = password
        self.room = room
        self.nick = nick
        self.__dict__.update(kwargs)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("groupchat_message", self.muc_message)

        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0045') # Multi-User Chat
        self.register_plugin('xep_0199') # XMPP Ping

    def session_start(self, event):
        self.get_roster()
        self.send_presence()

        self.plugin['xep_0045'].joinMUC(
            self.room,
            self.nick,
            password=getattr(self, 'room_password', None),
            wait=True,
            )

    def muc_message(self, msg):
        if msg['mucnick'] != self.nick:
            for handler in self.handlers:
                try:
                    result = handler(self, msg)
                except:
                    logger.logException(
                        'handler {} failed.'.format(handler.__name__))
                if not result:
                    continue
                if isinstance(result, str):
                    result = [result]
                for message in result:
                    self.send_message(
                        mto=msg['from'].bare,
                        mbody=message,
                        mtype='groupchat',
                        )
