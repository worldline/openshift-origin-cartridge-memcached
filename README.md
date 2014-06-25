# OpenShift Memcached Cartridge

The `memcached` cartridge provides [Memcached](http://www.memcached.org/) on OpenShift.

## Environment Variables

The `memcached` cartridge provides several environment variables to reference for ease
of use:

    OPENSHIFT_MEMCACHED_HOST      The Memcached IP address
    OPENSHIFT_MEMCACHED_PORT      The Memcached port

For more information about environment variables, consult the
[OpenShift Application Author Guide](https://github.com/openshift/origin-server/blob/master/node/README.writing_applications.md).

I also added 3 port mapping to communicate with Memcached from an external application :
	{Your openshift application url}/port11
	                                /port12
	                                /port14
	                                
You can use this reflector to install the cartridge :

	http://cartreflect-claytondev.rhcloud.com/reflect?github=dimsum12/openshift-origin-cartridge-memcached

