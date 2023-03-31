Name:		texlive-modular
Version:	44142
Release:	2
Summary:	Relative section headings for modular documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/modular
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modular.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modular.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX sections have absolute depth, e.g. \section, \subsection,
etc. When composing modular documents, we want relative depths.
The coseoul package provides relative headings, but does not
get things right when composing a document modularly from
multiple parts. This package provides the missing piece.
modular relies on coseoul, import, and ifthen.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/modular
%doc %{_texmfdistdir}/doc/latex/modular

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
