# import sys

# print("Starting here")
# # sys.exit("Interrupting hehehehe")
# print("Stop was here")

# db = {'wtp-mac': '00:ea:bd:0e:96:20', 'ip-addr': '10.225.23.195', 'name': 'CHA2-13-00075', 'device-detail': {'static-info': {'board-data': {'wtp-serial-num': 'FCW2230N2GF', 'wtp-enet-mac': '50:2f:a8:ec:89:94', 'ap-sys-info': {'mem-type': 'DDR4', 'cpu-type': ' ARMv7 Processor rev 1 (v7l)', 'mem-size': 1028096}}, 'board-data-opt': {'join-priority': 1}, 'descriptor-data': {'encryption-capabilities': True}, 'ap-prov': {'is-universal': False, 'universal-prime-status': 'Unprimed'}, 'ap-models': {'model': 'AIR-AP3802I-B-K9'}, 'num-ports': 8, 'num-slots': 3, 'wtp-model-type': 65, 'ap-capability': 'bridge-mode-capable cap-three-spatial-streams-capable avc-cnf-capable rxsop-threshold-capable fabric-capability barbados-internal-antenna-sku-capable remote-lan-capable dot11ac-160mhz-channel-width-capable avc-fnf-fabric-capable ap-cts-capable fips-capable is-dot1x-port-auth-capable ap-tracing-capable ap-wpa3-capable is-lag-capable office-extend-capable eth2-rlan-capable sniffer-mode-capable icap-partial-capable icap-anomaly-detection-capable icp-statistics-capable icap-rf-spectrum-capable icap-feature-capable ap-awips-capable iox-hardware-capable auxiliary-client-interface-capable ext-module-capable click-os-feature-set td-stats image-direct-download aid-manage-capable', 'is-mm-opt': False, 'ap-image-name': ''}, 'dynamic-info': {'led-state-enabled': True, 'reset-button-state': False, 'led-flash-enabled': True, 'flash-sec': 0, 'temp-info': {'degree': 0, 'temp-status': 'normal', 'heater-status': 'heater1-off-heater2-off'}}, 'wtp-version': {'backup-sw-version': {'version': 17, 'release': 6, 'maint': 1, 'build': 152}, 'sw-ver': {'version': 17, 'release': 6, 'maint': 2, 'build': 43}}}, 'ap-lag-enabled': False, 'ap-location': {'floor': 0, 'location': 'CHA2'}, 'ap-services': {'monitor-mode-opt-type': 'mode-type-none'}, 'tag-info': {'policy-tag-info': {
#     'policy-tag-name': 'AmazonDefault'}, 'site-tag': {'site-tag-name': 'default-site-tag'}, 'rf-tag': {'rf-tag-name': 'General_Use'}, 'filter-info': {'filter-name': 'general_use_ap_filter'}}, 'tunnel': {'preferred-mode': 'preferred-mode-ipv4', 'udp-lite': 'udplite-checksum-unconfigured'}, 'external-module-data': {'xm-data': {'is-module-present': False}, 'usb-data': {'is-module-present': False}, 'usb-override': False, 'is-ext-module-enabled': False}, 'ipv6-joined': 0, 'ap-state': {'ap-admin-state': 'adminstate-enabled', 'ap-operation-state': 'registered'}, 'ap-mode-data': {'ap-sub-mode': 'ap-sub-mode-none', 'wtp-mode': 'local-mode', 'ap-fabric-data': {'is-fabric-ap': False}}, 'ap-time-info': {'boot-time': '2022-02-17T10:08:53+00:00', 'join-time': '2022-02-17T13:36:08.763796+00:00'}, 'country-code': 'US ', 'ap-security-data': {'cert-type': 'wireless-cert-mic', 'ap-cert-policy': 'ap-cert-policy-default', 'ap-cert-expiry-time': '2029-05-14T20:25:41+00:00'}, 'num-radio-slots': 2, 'dart-is-connected': True, 'is-master': False, 'sliding-window': {'multi-window-support': True, 'window-size': 1}, 'cdp-enable': True, 'ap-stationing-type': 'indoor-ap', 'reboot-stats': {'reboot-reason': 'ap-reboot-reason-config-mwar', 'reboot-type': 'ap-reboot-spam-initiated'}, 'proxy-info': {'hostname': '', 'port': 0, 'no-proxy-list': ''}, 'image-size-eta': 0, 'image-size-start-time': '1970-01-01T00:00:00+00:00', 'image-size-percentage': 0, 'mdns-group-id': 0, 'mdns-rule-name': '', 'wlc-image-size-eta': 0, 'wlc-image-size-start-time': '1970-01-01T00:00:00+00:00', 'wlc-image-size-percentage': 0, 'disconnect-detail': {'disconnect-reason': 'wtp-found-configured-primary-mwar'}, 'wtp-ip': '10.225.23.195', 'lsc-status-pld-supported': [None], 'ap-lsc-status': {'is-dtls-lsc-enabled': False, 'is-dot1x-lsc-enabled': False, 'is-dtls-lsc-fallback': False}}

# dicky = {'wtp-mac': '00:ea:bd:0e:96:20', 'ip-addr': '10.225.23.195', 'name': 'CHA2-13-00075', 'device-detail': {'static-info': {'board-data': {'wtp-serial-num': 'FCW2230N2GF', 'wtp-enet-mac': '50:2f:a8:ec:89:94', 'ap-sys-info': {'mem-type': 'DDR4', 'cpu-type': ' ARMv7 Processor rev 1 (v7l)', 'mem-size': 1028096}}, 'board-data-opt': {'join-priority': 1}, 'descriptor-data': {'encryption-capabilities': True}, 'ap-prov': {'is-universal': False, 'universal-prime-status': 'Unprimed'}, 'ap-models': {'model': 'AIR-AP3802I-B-K9'}, 'num-ports': 8, 'num-slots': 3, 'wtp-model-type': 65, 'ap-capability': 'bridge-mode-capable cap-three-spatial-streams-capable avc-cnf-capable rxsop-threshold-capable fabric-capability barbados-internal-antenna-sku-capable remote-lan-capable dot11ac-160mhz-channel-width-capable avc-fnf-fabric-capable ap-cts-capable fips-capable is-dot1x-port-auth-capable ap-tracing-capable ap-wpa3-capable is-lag-capable office-extend-capable eth2-rlan-capable sniffer-mode-capable icap-partial-capable icap-anomaly-detection-capable icp-statistics-capable icap-rf-spectrum-capable icap-feature-capable ap-awips-capable iox-hardware-capable auxiliary-client-interface-capable ext-module-capable click-os-feature-set td-stats image-direct-download aid-manage-capable', 'is-mm-opt': False, 'ap-image-name': ''}, 'dynamic-info': {'led-state-enabled': True, 'reset-button-state': False, 'led-flash-enabled': True, 'flash-sec': 0, 'temp-info': {'degree': 0, 'temp-status': 'normal', 'heater-status': 'heater1-off-heater2-off'}}, 'wtp-version': {'backup-sw-version': {'version': 17, 'release': 6, 'maint': 1, 'build': 152}, 'sw-ver': {'version': 17, 'release': 6, 'maint': 2, 'build': 43}}}, 'ap-lag-enabled': False, 'ap-location': {'floor': 0, 'location': 'CHA2'}, 'ap-services': {'monitor-mode-opt-type': 'mode-type-none'}, 'tag-info': {'policy-tag-info': {
#     'policy-tag-name': 'AmazonDefault'}, 'site-tag': {'site-tag-name': 'default-site-tag'}, 'rf-tag': {'rf-tag-name': 'General_Use'}, 'filter-info': {'filter-name': 'general_use_ap_filter'}}, 'tunnel': {'preferred-mode': 'preferred-mode-ipv4', 'udp-lite': 'udplite-checksum-unconfigured'}, 'external-module-data': {'xm-data': {'is-module-present': False}, 'usb-data': {'is-module-present': False}, 'usb-override': False, 'is-ext-module-enabled': False}, 'ipv6-joined': 0, 'ap-state': {'ap-admin-state': 'adminstate-enabled', 'ap-operation-state': 'registered'}, 'ap-mode-data': {'ap-sub-mode': 'ap-sub-mode-none', 'wtp-mode': 'local-mode', 'ap-fabric-data': {'is-fabric-ap': False}}, 'ap-time-info': {'boot-time': '2022-02-17T10:08:53+00:00', 'join-time': '2022-02-17T13:36:08.763796+00:00'}, 'country-code': 'US ', 'ap-security-data': {'cert-type': 'wireless-cert-mic', 'ap-cert-policy': 'ap-cert-policy-default', 'ap-cert-expiry-time': '2029-05-14T20:25:41+00:00'}, 'num-radio-slots': 2, 'dart-is-connected': True, 'is-master': False, 'sliding-window': {'multi-window-support': True, 'window-size': 1}, 'cdp-enable': True, 'ap-stationing-type': 'indoor-ap', 'reboot-stats': {'reboot-reason': 'ap-reboot-reason-config-mwar', 'reboot-type': 'ap-reboot-spam-initiated'}, 'proxy-info': {'hostname': '', 'port': 0, 'no-proxy-list': ''}, 'image-size-eta': 0, 'image-size-start-time': '1970-01-01T00:00:00+00:00', 'image-size-percentage': 0, 'mdns-group-id': 0, 'mdns-rule-name': '', 'wlc-image-size-eta': 0, 'wlc-image-size-start-time': '1970-01-01T00:00:00+00:00', 'wlc-image-size-percentage': 0, 'disconnect-detail': {'disconnect-reason': 'wtp-found-configured-primary-mwar'}, 'wtp-ip': '10.225.23.195', 'lsc-status-pld-supported': [None], 'ap-lsc-status': {'is-dtls-lsc-enabled': False, 'is-dot1x-lsc-enabled': False, 'is-dtls-lsc-fallback': False}}

# import json

# print(json.dumps(dicky, indent=4))
# # for ap in db:
# #     print(ap)

class abc():
    def __init__(self, name) -> None:
        self.name = name
        return self.name # Not allowed

abc("nmaerr")