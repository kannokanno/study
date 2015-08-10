use strict;
use warnings;
use URI;
use Web::Scraper;
use Encode;

my $authors = scraper {
    process 'table[width="100%"] td', "authors[]" => scraper {
        process "a", uri => '@href';
        process "small", fullname => 'TEXT';
    };
};

my $res = $authors->scrape(URI->new("http://search.cpan.org/author/?A"));
for my $author (@{$res->{authors}}) {
    print Encode::encode("utf8", "$author->{fullname}\t$author->{uri}\n");
}
