Name:		texlive-pagella-otf
Version:	64705
Release:	2
Summary:	Using the OpenType fonts TeX Gyre Pagella
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagella-otf
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagella-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagella-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can only be used with LuaLaTeX or XeLaTeX. It does
the font setting for the OpenType font 'TeX Gyre Pagella' for
text and math. The missing typefaces like bold math and slanted
text are also defined

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pagella-otf
%doc %{_texmfdistdir}/doc/fonts/pagella-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
