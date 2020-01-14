
class Pub:
    def __init__(self, title, author, journal, year, number_pages, doi):
        self.title = title
        self.author = author
        self.journal = journal
        self.year = year
        self.number_pages = number_pages
        self.doi = doi

    def __repr__(self):
        return '{0} ({1}): {2}'.format(self.author, self.year, self.title)

    def to_html(self):
        return '{0} ({1}): {2}. <i>{3}</i>, {4} (<a href="https://doi.org/{5}">{5}</a>)'.format(
                self.author, self.year, self.title, self.journal, self.number_pages, self.doi)


journals = {
        'grl': 'Geophys. Res. Lett.',
        'jas': 'J. Atmos. Sci.',
        'gmd': 'Geosci. Model Dev.',
        'blm': 'Boundary Layer Meteorol.',
        'qjr': 'Q.J.R. Meteorol. Soc.',
        'jgra': 'J. Geophys. Res. Atmos.'
        }


reference = {
    'heerwaarden2017': Pub('MicroHH 1.0: a computational fluid dynamics code for direct numerical simulation and large-eddy simulation of atmospheric boundary layer flows',
        'C.C. van Heerwaarden, B.J.H. van Stratum, T. Heus, J. Gibbs, E. Fedorovich, J.P. Mellado',
        journals['gmd'], 2017, '10(8), 3145-3165', '10.5194/gmd-10-3145-2017'),
    }

papers = {
    'osman2019': Pub('Validating the water vapor variance similarity relationship in the interfacial layer using observations and large‐eddy simulations',
        'M.K. Osman, D.D. Turner, T. Heus, V. Wulfmeyer',
        journals['jgra'], 2019, '124, 10,662–10,675', '10.1029/2019JD030653'),

    'neggers2019': Pub('Power-Law Scaling in the Internal Variability of Cumulus Cloud Size Distributions due to Subsampling and Spatial Organization',
        'R.A.J. Neggers, P.J. Griewank, T. Heus',
        journals['jas'], 2019, '124, 76(6), 1489-1503', '10.1175/JAS-D-18-0194.1'),

    'anurose2019': Pub('Understanding the Moisture Variance in Precipitating Shallow Cumulus Convection',
        'T.J. Anurose, I. Bašták Ďurán, J. Schmidli, A. Seifert',
        journals['jgra'], 2019, '', '10.1029/2019JD031178'),

    'mol2019': Pub('Surface Moisture Exchange Under Vanishing Wind in Simulations of Idealized Tropical Convection',
        'W.B. Mol  C.C. van Heerwaarden, L. Schlemmer',
        journals['blm'], 2019, '46(22), 13602-13609', '10.1029/2019GL085047'),

    'linden2019': Pub('Large-Eddy Simulations of the Steady Wintertime Antarctic Boundary Layer',
        'S.J.A. van der Linden, J.M. Edwards, C.C. van Heerwaarden, E. Vignon, C. Genthon, I. Petenko, P. Baas, H.J.J. Jonker, B.J.H. van de Wiel',
        journals['blm'], 2019, '', '10.1007/s10546-019-00461-4'),

    'bosman2018': Pub('Sensible heating as a potential mechanism for enhanced cloud formation over temperate forest',
        'P.J.M. Bosman,  C.C. van Heerwaarden,  A.J. Teuling',
        journals['qjr'], 2018, '', '10.1002/qj.3441'),

    'hooijdonk2018': Pub('Parameters for the collapse of turbulence in the stratified plane Couette flow',
        'I.G. van Hooijdonk, H.J. Clercx, C. Ansorge, A.F. Moene, B.J.H. van de Wiel',
        journals['jas'], 2018, '75(9), 3211-3231', '10.1175/JAS-D-17-0335.1'),

    'duran2018': Pub('A Turbulence Scheme with Two Prognostic Turbulence Energies',
        'I. Bašták Ďurán, J.F. Geleyn, F. Váňa, J. Schmidli, R. Brožková',
        journals['jas'], 2018, '75(10), 3381-3402', '10.1175/JAS-D-18-0026.1'),

    'vanhooft2018': Pub('Towards Adaptive Grids for Atmospheric Boundary-Layer Simulations',
        'J.A. van Hooft, S. Popinet, C.C. van Heerwaarden, S.J.A. van der Linden, S.R. de Roode, B.J.H. van de Wiel',
        journals['blm'], 2018, '167(3), 421-433', '10.1007/s10546-018-0335-9'),

    'fedorovich2017': Pub('Numerical study of nocturnal low-level jets over gently sloping terrain',
        'E. Fedorovich,, J.A. Gibbs, A. Shapiro',
        journals['jas'], 2017, '74(9), 2813-2834', '10.1175/JAS-D-17-0013.1'),

    'mccol2017': Pub('Role of large eddies in the break- down of the Reynolds analogy in an idealized mildly unstable atmospheric surface layer',
        'K.A. McColl, C.C. van Heerwaarden, G.G. Katul, P. Gentine, D. Entekhabi',
        journals['qjr'], 2017, '143(706), 2182-2197', '10.1002/qj.3077'),

    'vanheerwaarden2016': Pub('Growth and Decay of a Convective Boundary Layer over a Surface with a Constant Temperature',
        'C.C. van Heerwaarden, J.P. Mellado',
        journals['jas'], 2016, '73(5), 2165-2177', '10.1175/JAS-D-15-0315.1'),

    'gentine2015': Pub('A Closer Look at Boundary Layer Inversion in Large-Eddy Simulations and Bulk Models: Buoyancy-Driven Case',
        'P. Gentine, G. Bellon, and C.C van Heerwaarden',
        journals['jas'], 2015, '72(2), 728-749', '10.1175/JAS-D-13-0377.1'),

    'vanheerwaarden2014': Pub('Scaling Laws for the Heterogeneously Heated Free Convective Boundary Layer',
        'C.C. van Heerwaarden, J.P. Mellado, A. De Lozar',
        journals['jas'], 2014, '71(11), 3975-4000', '10.1175/JAS-D-13-0383.1'),
    }

# Generate HTML
# 1. Find start and end years
minyear = 9999
maxyear = 0

for key,item in papers.items():
    minyear = min(minyear, item.year)
    maxyear = max(maxyear, item.year)

# 2. Put reference papers on top
print('<li><h4>Reference</h4></li>')
print('<ul>')
for key,item in reference.items():
    paper = item.to_html()
    print('    <li>{}</li>'.format(paper))
print('</ul>')

# 2. Print list of papers per year
for year in range(maxyear, minyear-1, -1):
    print('<li><h4>{}</h4></li>'.format(year))
    print('<ul>')
    for key,item in papers.items():
        if item.year == year:
            paper = item.to_html()
            print('    <li>{}</li>'.format(paper))
    print('</ul>')
