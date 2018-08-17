Role Name
=========

replace_node - Replace gluster node with a new node.

Requirements
------------

- Ansible >= 2.6
- lvm2 (Optional)


NOTE: Inventory should contain a single node, which should be part of the cluster. This node should be different than any of the three variables explained below, this requirement is to collect the right peers for the new node.

Role Variables
--------------

| Name                     |Choices| Default value         | Comments                          |
|--------------------------|-------|-----------------------|-----------------------------------|
| gluster_maintenance_old_node |    | UNDEF   | The node which has to be replaced with a new node. Just the node name is needed to get the peer id, the node need not be accessible. Provide the name that was used to probe the peers. |
| gluster_maintenance_new_node |   | UNDEF | New node which will replace the old node. This name can be same as the old node or different name. |
| gluster_maintenance_cluster_node |  | UNDEF | The node on which the peer, volume-id details are collected. This node should be part of the trusted storage pool. And should be different from old_node or new_node. |
| gluster_maintenance_ovirt_url |  | UNDEF | URL for the ovirt management node |
| gluster_maintenance_ovirt_username | | UNDEF | Username for ovirt management node authentication |
| gluster_maintenance_ovirt_password |  | UNDEF | Password for ovirt management node login |
| gluster_maintenance_ovirt_cafile | | UNDEF | A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. |
| gluster_maintenance_ovirt_mgmt_host | | UNDEF | This is a mandatory variable if the hosts have to be moved to maintenance/active mode. This is the management hostname, passwordless ssh has to be set to this machine. |


Dependencies
------------

Depends on:

- gluster.repositories (Optional: to subscribe to channels)
- gluster.infra (Optional: to setup bricks)

Example Playbook
----------------

Note that `server' in the inventory and the variable gluster_maintenance_cluster_node are unique (if the number of nodes are more than 2).

```
---
- remote_user: root
  gather_facts: no
  hosts: server
  vars:
    - gluster_maintenance_old_node: store
    - gluster_maintenance_new_node: store
    - gluster_maintenance_cluster_node: data
  roles:
    - gluster.maintenance
```

In the above example, a new host named store will replace the old host (the replaced node has the same hostname as the old node, however ensure that old node is not accessible with the hostname, else the results are undefined.


License
-------

GPLv3
