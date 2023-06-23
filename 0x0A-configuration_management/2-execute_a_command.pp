# This process kills killmenow
exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin'
}
