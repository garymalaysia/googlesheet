#!/usr/local/bin/perl
use List::Compare;
use Array::Utils;
 #use strict;
 #use warnings;

open  $fh1, '<', 'text.txt' or die $!;

#seecond data file
open $fh2, '<', 'text2.txt' or die $!;

#output file
open OUTPUT, '>', 'cCheck.txt' or die $!;

while ( !eof($fh1) and !eof ($fh2) ) {

	$line1 = <$fh1>;
	$line2 = <$fh2>;
	@host = split /,/,$line1;
	@os = split /,/ , $line2;
	
	#@host = $host[0];
	#@string = split //,$string1;
	foreach ($host[0]){

		@string1 = $host[0];	
	}
print @string1[0];
	#$string1=  @host[0], "\n" if @host[16]=~ /'Credentialed checks : no'/;
	#@string2=  @os[0], "\n" if  @os[1]=~ /Microsoft/;	
	#@string1 = split / /,$string1;
	#@string2 = split /''/, @string2;
#print @string1[0];
#print OUTPUT @host[0];


}


	
print "Executing perl script...\n";
#my $status = system ("python google.py");


close ($fh1);
close($fh2);
close (OUTPUT);