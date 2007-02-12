# TODO
# - uses cpaint.sf.net (create package?)
# - apache config or sth?
Summary:	AJAX spell checker
Summary(pl.UTF-8):   AJAX - narzędzie do sprawdzania pisowni
Name:		ajax-spell
Version:	2.2
Release:	1
Epoch:		0
License:	BSD
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/ajax-spell/spell_checker-%{version}.zip
# Source0-md5:	7574b0c1f6635301533f914be7caea2b
Patch0:		%{name}-fixes.patch
URL:		http://www.broken-notebook.com/spell_checker/
Requires:	pspell
Requires:	webserver(php) >= 4.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AJAX spell checker for text areas using PHP, JavaScript, and pspell /
aspell.

%description -l pl.UTF-8
AJAX to narzędzie do sprawdzania pisowni dla pól tekstowych przy
użyciu PHP, JavaScriptu oraz pspella/aspella.

%prep
%setup -q -c
# undos the source
find . -type f -print0 | xargs -0 sed -i -e 's,
$,,'
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -a *.js *.php *.css $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.txt
%{_datadir}/%{name}
