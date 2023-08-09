# Fix typo found using strace
exec { 'Fixing typo':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
