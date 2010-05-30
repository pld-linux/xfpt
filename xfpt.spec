Summary:	XML From Plain Text
Name:		xfpt
Version:	0.07
Release:	1
License:	GPL v2
Group:		Applications/Publishing/XML
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/wordprocessing/unix/xfpt/%{name}-%{version}.tar.bz2
# Source0-md5:	6e2aea16cf1df347ffd57b27de654a05
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfpt is a program that reads a file of plain text that contains
relatively simple markup, and outputs an XML file. It is intended to
simplify the management of XML data. It is not a program that attempts
to turn a plain text document into XML. Markup within text is
introduced by ampersand characters, but is otherwise "soft". You can
define what follows the ampersand, for example, &" to generate a
"quote" element. There is also a macro facility that allows for higher
level concepts such as chapters, displays, tables, etc.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DATADIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfpt
%{_datadir}/xfpt
%{_mandir}/man1/xfpt.1*
