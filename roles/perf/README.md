perf
====

Runs performance tests on the nodes and gathers the results.

Requirements
------------

gluster-ansible
netperf3
fio
python-firewall* - This should not be python3-firewall. This is Ansible module requirement

Role Variables
--------------

| Name                     | Required? | Choices| Default value         | Comments |
|--------------------------|----|---|-----------------------|-----------------------------------|
| gluster_maintenance_volname | yes | | UNDEF | The GlusterFS volume name, whose performance has to be evaluated |
| gluster_maintenance_mountpoint | yes | | UNDEF | GlusterFS' Mountpoint |
| gluster_maintenance_client | yes || UNDEF | The hostname/ip of the GlusterFS client |
| gluster_maintenance_vm is defined | yes || The VM whose image resides on GlusterFS mountpoint |
| gluster_maintenance_net_perf_nodes | Yes |  | UNDEF   | List of nodes on which to collect the network performance numbers. |
| gluster_maintenance_net_ping_duration | No |  | 10 | Ping counter |
| gluster_maintenance_net_iperf_duration | No |  | 30 | iperf timer; time in seconds to transmit for |
| gluster_maintenance_net_fio_numjobs | No | | 16 | Number of fio jobs to run |
| gluster_maintenance_fio_size_gb | No | | 16G | The allowable file size upto which fio job can write |
| gluster_maintenance_monitor_interval | No | | 10 | The monitor interval for sar utility |

Dependencies
------------

netperf3

Example Playbook
----------------

---
- remote_user: root
  gather_facts: no
  hosts: hc-nodes
  vars:
    - gluster_maintenance_net_perf_nodes:
        - 10.70.42.11
        - 10.70.42.231
        - 10.70.41.209
    - gluster_maintenance_volname: expr
    - gluster_maintenance_mountpoint: /mnt/glusterfs
    - gluster_maintenance_client: 10.70.42.178
    - gluster_maintenance_vm: 10.70.42.231
    - gluster_maintenance_fio_size_gb: 5
    - gluster_maintenance_fio_numjobs: 5
  roles:
    - gluster.maintenance


License
-------

GPLv3

