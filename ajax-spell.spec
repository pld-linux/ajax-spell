# TODO
# - uses cpaint.sf.net (create package?)
# - apache config or sth?
Summary:	AJAX spell checker
Name:		ajax-spell
Version:	2.1
Release:	0.4
Epoch:		0
License:	BSD
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/ajax-spell/spell_checker-%{version}.zip
# Source0-md5:	50010f24b22342e18f9c89944c28b763
Patch0:		%{name}-fixes.patch
URL:		http://www.broken-notebook.com/spell_checker/
Requires:	php >= 3:4.3.0
Requires:	pspell
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AJAX spell checker for text areas using PHP, Javascript, and pspell /
aspell.

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
