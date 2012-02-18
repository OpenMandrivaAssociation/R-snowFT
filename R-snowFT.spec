%global packname  snowFT
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.2_0
Release:          1
Summary:          Fault Tolerant Simple Network of Workstations
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-snow 
Requires:         R-rpvm R-Rmpi R-rlecuyer R-rsprng 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-snow
BuildRequires:    R-rpvm R-Rmpi R-rlecuyer R-rsprng 

%description
Extension of the snow package supporting fault tolerant and reproducible
applications, as well as supporting easy-to-use parallel programming -
only one function is needed.

%prep
%setup -q -c -n %{packname}

perl -pi -e 's|\brmpi\b|Rmpi|;' snowFT/man/snowFT-package.Rd snowFT/DESCRIPTION

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
