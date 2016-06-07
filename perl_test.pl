#!/usr/local/bin/perl
use List::Compare;
use Array::Utils;
 use strict;
 #use warnings;

open my $fh1, '<', 'text.txt' or die $!;

#seecond data file
open my $fh2, '<', 'text2.txt' or die $!;

#output file
open OUTPUT, '>', 'cCheck.txt' or die $!;
open my $fh3, '<', 'text3.txt' or die $!;
open my $fh4, '<', 'text4.txt' or die $!;

while ( !eof($fh1) and !eof ($fh2) ) {

	my $line1 = <$fh1>;
	my $line2 = <$fh2>;
	my $line3 = <$fh3>;
	my $line4 = <$fh4>;
	my @host = split /,/,$line1;
	my @os = split /,/ , $line2;
	my @line3 = split / /, $line3;
	
	my $string1=  join(' ', @host[0]), "\n\n" if @host[16]=~ /'Credentialed checks : no'/;
	my @string1= split(/ /, $string1);
	my $string2=  @os[0], "\n\n" if  @os[1]=~ /Microsoft/;	
	#my @string1 = split / /,$os[0];
	#my @string2 = split /''/, $host[0];
print @string1[0];


}



	
print "Executing perl script...\n";
#my $status = system ("python google.py");


close ($fh1);
close($fh2);
close($fh3);
close($fh4);
close (OUTPUT);