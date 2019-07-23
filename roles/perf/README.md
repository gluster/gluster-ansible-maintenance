network_perf
=========

Gathers the network performance on the nodes

Requirements
------------

gluster-ansible
netperf3

Role Variables
--------------

| Name                     | Required? | Choices| Default value         | Comments |
|--------------------------|----|---|-----------------------|-----------------------------------|
| gluster_maintenance_net_nodes | Yes |  | UNDEF   | List of nodes on which to collect the network performance numbers. |
| gluster_maintenance_net_single | No |  | First node in the list | Collect the perf numbers from all nodes to one lead host |
| gluster_maintenance_net_ping_duration | No |  | 10 | Ping counter |
| gluster_maintenance_net_iperf_duration | No |  | 30 | iperf timer; time in seconds to transmit for |

Dependencies
------------

netperf3

Example Playbook
----------------


    - hosts: servers
      TODO
      roles:
         - gluster.maintenance

License
-------

GPLv3

