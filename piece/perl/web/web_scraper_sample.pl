use strict;
use warnings;
use URI;
use Web::Scraper;
use Encode;

sub cpan_authors {
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
}

sub print_hatebu {
    my $url = 'http://b.hatena.ne.jp/search/text?q=vim';
    my $client = scraper {
        process '.search-result-list li', "titles[]" => scraper {
            process "a", title => '@title';
        };
    };
    my $res = $client->scrape(URI->new($url));
    for (@{$res->{titles}}) {
        print "$_->{title}\n";
    }
}

print_hatebu();
