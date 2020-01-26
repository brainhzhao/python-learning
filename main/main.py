
import utils.netutil.sendmsg
import model.student
import model.interface

if __name__ == "__main__1":
   message = '''<124>Feb 8 14:47:01 H3C data_type1=attack97;log_type2=alerti20;attack_name4=151003403OpenSSL CVE-2014-0224 Man in the Middle Security Bypass Vulnerability Scan7;app_protocol_name6=84021364HTTPS13;protocol7=656;segment_direct28=72;src_ip22=192.130.12.62 ;src_port23=134b;dst_ip24=171.89.207.143;dst_port25=1111;ifname_in16=xeth0/0;ifname_out17=xeth0/0;aggre_count26=1;aggre_offset43=0;vlan125=;smac126=00:01:d7:ec:e5:04;dmac127=54:75:d0:5b:1d:8c;agent_ip128=1.1.1.1'''
   send_msg = SendMessage('10.65.133.156',1024)
   send_msg.send_by_udp(message,1000,1000)

if __name__ == "__main__":
    print help(type(utils))
