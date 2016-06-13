#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-jwt
Version  : 1.5.4
Release  : 11
URL      : https://rubygems.org/downloads/jwt-1.5.4.gem
Source0  : https://rubygems.org/downloads/jwt-1.5.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rubygems-tasks
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-json

%description
# JWT
[![Build Status](https://travis-ci.org/jwt/ruby-jwt.svg)](https://travis-ci.org/jwt/ruby-jwt)
[![Code Climate](https://codeclimate.com/github/jwt/ruby-jwt/badges/gpa.svg)](https://codeclimate.com/github/jwt/ruby-jwt)
[![Test Coverage](https://codeclimate.com/github/jwt/ruby-jwt/badges/coverage.svg)](https://codeclimate.com/github/jwt/ruby-jwt/coverage)
[![Issue Count](https://codeclimate.com/github/jwt/ruby-jwt/badges/issue_count.svg)](https://codeclimate.com/github/jwt/ruby-jwt)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n jwt-1.5.4
gem spec %{SOURCE0} -l --ruby > rubygem-jwt.gemspec

%build
gem build rubygem-jwt.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
jwt-1.5.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/jwt-1.5.4.gem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/.codeclimate.yml
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/Manifest
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/README.md
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/lib/jwt.rb
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/lib/jwt/decode.rb
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/lib/jwt/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/lib/jwt/json.rb
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/lib/jwt/verify.rb
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/lib/jwt/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/ruby-jwt.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec256-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec256-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec256-wrong-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec256-wrong-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec384-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec384-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec384-wrong-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec384-wrong-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec512-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec512-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec512-wrong-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/ec512-wrong-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/rsa-1024-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/rsa-1024-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/rsa-2048-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/rsa-2048-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/rsa-2048-wrong-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/rsa-2048-wrong-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/rsa-4096-private.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/fixtures/certs/rsa-4096-public.pem
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/jwt/verify_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/jwt_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/jwt-1.5.4/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/jwt-1.5.4.gemspec
