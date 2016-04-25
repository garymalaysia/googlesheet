#!/usr/local/bin/perl
use strict;
use warnings;

open(INPUT, "<text.txt");
open(OUTPUT, ">no_comma.txt");
while (<INPUT>) {


if (m/\n+/g){
		$_=~ s/\,+/ /g;
		$_ =~ s/\n//g;

	}
	
else{
		$_=~ s/\,+/ /g;
		$_ =~ s/\s+/\n/g;
}
	
	my @text = split (/ /,$_);
	
	
		

		print OUTPUT  "@text\n" ;

}
	
print "Done! Go check 'no_comma.txt'\n";
my $status = system ("python google.py");


close (INPUT);
close (OUTPUT);