import os
from enum import Enum

PROXY = {
    # 'http': 'socks5://127.0.0.1:1080',
    # 'https': 'socks5://127.0.0.1:1080'
}


class DOMAIN(Enum):
    nhentai_net = "nhentai.net"
    ehentai_org = "ehentai.org"
    wnacg_com = "wnacg.com"


COMIC_ROOT_PATH = '/storage/comic'

# ------------------------------------------------------------

COMIC_MAIN_PATH = os.path.abspath(os.curdir) + COMIC_ROOT_PATH
COMIC_PATHS = {
    DOMAIN.nhentai_net: '%s/%s' % (COMIC_MAIN_PATH, DOMAIN.nhentai_net.value),
    DOMAIN.ehentai_org: '%s/%s' % (COMIC_MAIN_PATH, DOMAIN.ehentai_org.value),
    DOMAIN.wnacg_com: '%s/%s' % (COMIC_MAIN_PATH, DOMAIN.wnacg_com.value)
}
COMIC_DOWNLOADING_PATHS = {
    DOMAIN.nhentai_net: '%s/downloading' % (COMIC_PATHS[DOMAIN.nhentai_net]),
    DOMAIN.ehentai_org: '%s/downloading' % (COMIC_PATHS[DOMAIN.ehentai_org]),
    DOMAIN.wnacg_com: '%s/downloading' % (COMIC_PATHS[DOMAIN.wnacg_com]),
}
