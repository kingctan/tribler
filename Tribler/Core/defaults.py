# Written by Arno Bakker and Bram Cohen
# Updated by George Milescu
# see LICENSE.txt for license information
""" Default values for all configurarable parameters of the Core"""
#
# For an explanation of each parameter, see SessionConfig/DownloadConfig.py
#
# defaults with comments behind them are not user-setable via the
# *ConfigInterface classes, because they are not currently implemented (IPv6)
# or we only use them internally.
#
# WARNING:
#    As we have release Tribler 4.5.0 you must now take into account that
#    people have stored versions of these params on their disk. Make sure
#    you change the version number of the structure and provide upgrade code
#    such that your code won't barf because we loaded an older version from
#    disk that does not have your new fields.
#
import sys
import os
from simpledefs import *
from collections import OrderedDict

DEFAULTPORT = 7760

#
# Session opts
#
# History:
#  Version 2: as released in Tribler 4.5.0
#
SESSDEFAULTS_VERSION = 2
sessdefaults = OrderedDict()

# General Tribler settings
sessdefaults['general'] = OrderedDict()
sessdefaults['general']['version'] = SESSDEFAULTS_VERSION
sessdefaults['general']['state_dir'] = None
sessdefaults['general']['install_dir'] = u'.'
sessdefaults['general']['ip'] = ''
sessdefaults['general']['minport'] = DEFAULTPORT
sessdefaults['general']['maxport'] = DEFAULTPORT
sessdefaults['general']['bind'] = []
sessdefaults['general']['ipv6_enabled'] = 0  # allow the client to connect to peers via IPv6 (currently not supported)
sessdefaults['general']['ipv6_binds_v4'] = None  # set if an IPv6 server socket won't also field IPv4 connections (default = set automatically)
sessdefaults['general']['timeout'] = 300.0
sessdefaults['general']['timeout_check_interval'] = 60.0
sessdefaults['general']['eckeypairfilename'] = None
sessdefaults['general']['megacache'] = True
sessdefaults['general']['nickname'] = '__default_name__'  # is replaced with hostname in LaunchManyCore.py
sessdefaults['general']['mugshot'] = None
sessdefaults['general']['videoanalyserpath'] = None
sessdefaults['general']['peer_icon_path'] = None
sessdefaults['general']['live_aux_seeders'] = []

# Mainline DHT settings
sessdefaults['mainline_dht'] = OrderedDict()
sessdefaults['mainline_dht']['enabled'] = True
sessdefaults['mainline_dht']['mainline_dht_port'] = -1

# Torrent checking settings
sessdefaults['torrent_checking'] = OrderedDict()
sessdefaults['torrent_checking']['enabled'] = 1
sessdefaults['torrent_checking']['torrent_checking_period'] = 31  # will be changed to min(max(86400/ntorrents, 15), 300) at runtime

# Torrent collecting settings
sessdefaults['torrent_collecting'] = OrderedDict()
sessdefaults['torrent_collecting']['enabled'] = True
sessdefaults['torrent_collecting']['dht_torrent_collecting'] = True
sessdefaults['torrent_collecting']['torrent_collecting_max_torrents'] = 50000
sessdefaults['torrent_collecting']['torrent_collecting_dir'] = None
sessdefaults['torrent_collecting']['stop_collecting_threshold'] = 200

# Libtorrent settings
sessdefaults['libtorrent'] = OrderedDict()
sessdefaults['libtorrent']['enabled'] = True
sessdefaults['libtorrent']['lt_proxytype'] = 0  # no proxy server is used by default
sessdefaults['libtorrent']['lt_proxyserver'] = None
sessdefaults['libtorrent']['lt_proxyauth'] = None
sessdefaults['libtorrent']['utp'] = True

# SWIFTPROC config
sessdefaults['swift'] = OrderedDict()
sessdefaults['swift']['enabled'] = True
sessdefaults['swift']['swiftpath'] = None
sessdefaults['swift']['swiftworkingdir'] = '.'
sessdefaults['swift']['swiftcmdlistenport'] = -1
sessdefaults['swift']['swiftdlsperproc'] = 1000
sessdefaults['swift']['swiftmetadir'] = None
# Config for tunneling via swift, e.g. dispersy
sessdefaults['swift']['swifttunnellistenport'] = DEFAULTPORT - 2
sessdefaults['swift']['swifttunnelhttpgwlistenport'] = -1
sessdefaults['swift']['swifttunnelcmdgwlistenport'] = -1
sessdefaults['swift']['swiftdhtport'] = -1

# Dispersy config
sessdefaults['dispersy'] = OrderedDict()
sessdefaults['dispersy']['enabled'] = True
sessdefaults['dispersy']['dispersy-tunnel-over-swift'] = False
sessdefaults['dispersy']['dispersy_port'] = DEFAULTPORT - 1

#
# BT per download opts
#
# History:
#  Version 2: as released in Tribler 4.5.0
#  Version 3:
#  Version 4: allow users to specify a download directory every time
#  Version 6: allow users to overwrite the multifile destination
#  Version 7: swift params
DLDEFAULTS_VERSION = 7
dldefaults = {}
dldefaults['version'] = DLDEFAULTS_VERSION
dldefaults['max_uploads'] = 7
dldefaults['keepalive_interval'] = 120.0
dldefaults['download_slice_size'] = 2 ** 14
dldefaults['upload_unit_size'] = 1460
dldefaults['request_backlog'] = 10
dldefaults['max_message_length'] = 2 ** 23
dldefaults['selector_enabled'] = 1  # whether to enable the file selector and fast resume function. Arno, 2009-02-9: Must be on for checkpoints to work.
dldefaults['expire_cache_data'] = 10  # the number of days after which you wish to expire old cache data (0 = disabled)
dldefaults['priority'] = []  # a list of file priorities separated by commas, must be one per file, 0 = highest, 1 = normal, 2 = lowest, -1 = download disabled'
dldefaults['saveas'] = None  # Set to get_default_destdir()
dldefaults['showsaveas'] = True  # Allow users to choose directory for every new download
dldefaults['max_slice_length'] = 2 ** 17
dldefaults['max_rate_period'] = 20.0
dldefaults['upload_rate_fudge'] = 5.0
dldefaults['tcp_ack_fudge'] = 0.03
dldefaults['rerequest_interval'] = 300
dldefaults['min_peers'] = 20
dldefaults['http_timeout'] = 60
dldefaults['max_initiate'] = 40
dldefaults['check_hashes'] = 1
dldefaults['max_upload_rate'] = 0
dldefaults['max_download_rate'] = 0
# Arno, 2009-12-11: Sparse as default reduces CPU usage. Previously this was
# also set, but in DownloadConfig.__init__
if sys.platform == 'win32':
    dldefaults['alloc_type'] = DISKALLOC_NORMAL
else:
    dldefaults['alloc_type'] = DISKALLOC_SPARSE
dldefaults['alloc_rate'] = 2.0
dldefaults['buffer_reads'] = 1
dldefaults['write_buffer_size'] = 4
dldefaults['breakup_seed_bitfield'] = 1
dldefaults['snub_time'] = 30.0
dldefaults['rarest_first_cutoff'] = 2
dldefaults['rarest_first_priority_cutoff'] = 5
dldefaults['min_uploads'] = 4
dldefaults['max_files_open'] = 20
dldefaults['round_robin_period'] = 30
dldefaults['super_seeder'] = 0
dldefaults['security'] = 1
dldefaults['max_connections'] = 0
dldefaults['auto_kick'] = 1
dldefaults['double_check'] = 0
dldefaults['triple_check'] = 0
dldefaults['lock_files'] = 0
dldefaults['lock_while_reading'] = 0
dldefaults['auto_flush'] = 0
#
# Tribler per-download opts
#
dldefaults['exclude_ips'] = ''
dldefaults['mode'] = 0
dldefaults['vod_usercallback'] = None
dldefaults['vod_userevents'] = []
dldefaults['video_source'] = None
dldefaults['video_ratelimit'] = 0
dldefaults['video_source_authconfig'] = None
dldefaults['selected_files'] = []

# Niels: in total uTorrent and Azureus clients agree not to accept more than 50 added peers
# http://wiki.theory.org/BitTorrentPeerExchangeConventions
dldefaults['ut_pex_max_addrs_from_peer'] = 50
# Version 3:
dldefaults['same_nat_try_internal'] = 0
dldefaults['unchoke_bias_for_internal'] = 0
# Version 6: add correctedfilename option
dldefaults['correctedfilename'] = None

# SWIFTPROC v7
dldefaults['swiftlistenport'] = None
dldefaults['swiftcmdgwlistenport'] = None
dldefaults['swifthttpgwlistenport'] = None
dldefaults['swiftmetadir'] = None

tdefdictdefaults = {}
tdefdictdefaults['comment'] = None
tdefdictdefaults['created by'] = None
tdefdictdefaults['announce'] = None
tdefdictdefaults['announce-list'] = None
tdefdictdefaults['nodes'] = None  # mainline DHT
tdefdictdefaults['httpseeds'] = None
tdefdictdefaults['url-list'] = None
tdefdictdefaults['encoding'] = None

tdefmetadefaults = {}
tdefmetadefaults['version'] = 1
tdefmetadefaults['piece length'] = 0
tdefmetadefaults['makehash_md5'] = 0
tdefmetadefaults['makehash_crc32'] = 0
tdefmetadefaults['makehash_sha1'] = 0
tdefmetadefaults['createmerkletorrent'] = 0
tdefmetadefaults['torrentsigkeypairfilename'] = None
tdefmetadefaults['thumb'] = None  # JPEG data

tdefdefaults = {}
tdefdefaults.update(tdefdictdefaults)
tdefdefaults.update(tdefmetadefaults)
