from .jid import JID, prep_localpart, prep_host


def _validate_jid(value):
    try:
        return JID(value)
    except:
        return None


def validate_jid(value):
    jid = _validate_jid(value)
    return None if jid is None else jid.full()


def validate_bare_jid(value):
    jid = _validate_jid(value)
    return None if jid is None else jid.userhost()


def validate_localpart(value):
    try:
        return prep_localpart(value)
    except:
        return None


def validate_host(value):
    try:
        return prep_host(value)
    except:
        return None
