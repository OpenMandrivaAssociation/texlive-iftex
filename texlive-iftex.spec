%global tl_name iftex
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0g
Release:	%{tl_revision}.1
Summary:	Am I running under pdfTeX, XeTeX or LuaTeX?
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/iftex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iftex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iftex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package, which works both for Plain TeX and for LaTeX, defines the
\ifPDFTeX, \ifXeTeX, and \ifLuaTeX conditionals for testing which engine
is being used for typesetting. The package also provides the
\RequirePDFTeX, \RequireXeTeX, and \RequireLuaTeX commands which throw
an error if pdfTeX, XeTeX or LuaTeX (respectively) is not the engine in
use.

