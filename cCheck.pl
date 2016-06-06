#!/usr/local/bin/perl

open(INPUT, "<text.txt");
open(OUTPUT, ">cCheck.txt");
while (<INPUT>) {
#@array = split /''/, $_;
@host = split /,/,$_;


#@string= @host[0].''.@host[28];


print OUTPUT  "@host[0]\n" ;

}

	
print "Executing perl script...\n";
#my $status = system ("python google.py");


close (INPUT);
close (OUTPUT);