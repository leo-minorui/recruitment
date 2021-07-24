```shell
docker run -p 389:389 -p 636:636 --name saasops-openldap-container --env LDAP_ORGANISATION='SAASOPS' --env LDAP_DOMAIN='SAASOPS.com' --env LDAP_ADMIN_PASSWORD='Sangforsaasops123.' --detach osixia/openldap:1.4.0

docker run -p 80:80 -p 443:443 --name phpldapadmin-service --hostname phpldapadmin-service --link saasops-openldap-container:ldap-host --env PHPLDAPADMIN_LDAP_HOSTS=ldap-host --detach osixia/phpldapadmin:0.9.0
```
管理员账号密码：

cn=admin,dc=SAASOPS,dc=com
Sangforsaasops123.
