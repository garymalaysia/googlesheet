#!/usr/local/bin/perl

open $fh1, '<', 'text.txt' or die $!;

#seecond data file
open $fh2, '<', 'text2.txt' or die $!;

#output file
open OUTPUT, '>', 'cCheck.txt' or die $!;

$x=0;
while ( !eof($fh1) and !eof ($fh2)) {

	$line1 = <$fh1>;
	$line2 = <$fh2>;
	@host = split /,/,$line1;
	@os = split /,/ , $line2;
	$size_host=@host;
	$size_os = @os;
	print "@os[0]\n", ;
#@string= $os[x].''.$os[1];
#print $out @host[0];
#if ($host[0]==$os[0]){
	
#print OUTPUT @string, "\n\n" if @host[16]=~ m/'Credentialed checks : no'/ ;

#}
#{
	#@string= @host[0].''.@host[16];

#}
#print $out "$os[1]\n" ;

}



	
print "Executing perl script...\n";
#my $status = system ("python google.py");


close ($fh1);
close($fh2);
close ($out);