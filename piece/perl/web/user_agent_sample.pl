use strict;
use warnings;
use LWP::UserAgent;
use Encode;

my $ua = LWP::UserAgent->new;
my $res = $ua->get('http://b.hatena.ne.jp/search/text?q=vim');

print $res->content;
