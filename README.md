[![build-test](https://github.com/darkwizard242/ansible-role-logrotate/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-logrotate/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-logrotate/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-logrotate/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47557?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/47557?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47557?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-logrotate&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-logrotate) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-logrotate&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-logrotate) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-logrotate&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-logrotate) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-logrotate&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-logrotate) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-logrotate?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-logrotate?color=orange&style=flat-square)

# Ansible Role: logrotate

Role to install (_by default_) [logrotate](https://github.com/logrotate/logrotate) package or uninstall (_if passed as var_) as well as configure for any number of logrotate configurations on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
logrotate_app: logrotate
logrotate_desired_state: present
logrotate_config_dir: /etc/logrotate.d
logrotate_configs: []
logrotate_template: conf.j2
```

### Variables table:

Variable                | Description
----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
logrotate_app           | Defines the app to install i.e. **logrotate**
logrotate_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.
logrotate_config_dir    | Directory to place logrotate configuration into i.e. **/etc/logrotate.d**
logrotate_configs       | Pass desired logrotate configurations. Playbook example provided.
logrotate_template      | Template used as source.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **logrotate** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.logrotate
```

For customizing behavior of role (i.e. custom config of **logrotate** ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.logrotate
  vars:
    logrotate_configs:
      - name: ansible
        path: /var/log/ansible.log
        options:
          - weekly
          - create 0644 root root
          - size 10M
          - rotate 5
          - dateext
          - dateformat -%Y_%m_%d
          - notifempty
          - missingok
          - compress
          - delaycompress
          - copytruncate
```

For customizing behavior of role (i.e. custom config and postrotate scripts of **logrotate** ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.logrotate
  vars:
    logrotate_configs:
      - name: ansible
        path: /var/log/ansible.log
        options:
          - weekly
          - create 0644 root root
          - size 10M
          - rotate 5
          - dateext
          - dateformat -%Y_%m_%d
          - notifempty
          - missingok
          - compress
          - delaycompress
          - copytruncate

      - name: ansible-script
        path: /var/log/ansible.log
        options:
          - weekly
          - create 0644 root root
          - size 10M
          - rotate 5
          - dateext
          - dateformat -%Y_%m_%d
          - notifempty
          - missingok
          - compress
          - delaycompress
          - copytruncate
        scripts:
          postrotate: 'echo "Ansible log has been rotated" > ~/rotation.txt'
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-logrotate/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
