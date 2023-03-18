import network

class IFCONFIG:
    def is_connect():
        sta_if = network.WLAN(network.STA_IF)
        return sta_if.isconnected()

    def get_address():
        if IFCONFIG.is_connect:
            sta_if = network.WLAN(network.STA_IF)
            data = sta_if.ifconfig()
            return data[0]

        return 'XXX'
