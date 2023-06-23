# This is a puppet code to crteate a file

file { '/tmp/school':
            ensure  => present,
            path    => '/tmp/school',
            mode    => '0744',
            owner   => 'www-data',
            group   => 'www-data',
            content => 'I love Puppet',
}
