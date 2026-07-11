%global tl_name modular
%global tl_revision 44142

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Relative section headings for modular documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/modular
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modular.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modular.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX sections have absolute depth, e.g. \section, \subsection, etc.
When composing modular documents, we want relative depths. The coseoul
package provides relative headings, but does not get things right when
composing a document modularly from multiple parts. This package
provides the missing piece. modular relies on coseoul, import, and
ifthen.

