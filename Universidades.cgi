#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use Text::CSV;
use Encode qw(encode decode);

my $cgi = CGI->new;
my $Busqueda =uc($cgi-> param('Busqueda por seleccion'))|| '';
my $solicitud =uc($cgi-> param('linkArchivo'));

print $cgi->header(-type => 'text/html', -charset => 'latin-1');
print $cgi->start_html('Solicitud del archivo CSV');
#obtener csv
my $csv_file = 'C:\Users\Usuario\Downloads\Programas de Universidades_4 (1).csv';
my $csv = Text::CSV->new ({ binary => 1, auto_diag => 1, sep_char => '|'});
open my $archivo, '<:encoding(latin-1)', $csv_file or die "Programas de Universidades_4(1).csv: $!";

#Busqueda por columna de nombre datos
my $header = $csv->getline($archivo);
my @resultados;
while(my $fila = $csv->getline($archivo)){
    my %campo;
    @campo{@$header} = @$fila;
    if ($campo{'NOMBRE'} eq $solicitud ||
        $campo{'PERIODO_LICENCIAMIENTO'} eq $solicitud ||
        $campo{'DEPARTAMENTO_LOCAL'} eq $solicitud ||
        $campo{'DENOMINACION_PROGRAMA'} eq $solicitud) {
        if($campo{'NOMBRE'} ne ''){ #valida si nombre no esta vacio
            push @resultados, \%campo; 
        }
    
    }
}
# Cerrar el archivo CSV
close $archivo;

#HTML para formato de la tabla de Resultados
print <<HTML;
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="latin-1">
    <title>Resultado de la Consulta</title>
</head>
<body>
    <div class="titulo1" style="text-align:center;">
        <h1>RESULTADO DE LA CONSULTA</h1>
    </div>
    <div class="cabezera">
        <table  border="1" style="text-align:center;">
            <tr>
                <th style="color: #b10c0c;">Nombre de Universidad</th>
                <th style="color: #b10c0c;">Periodo de Licenciamiento</th>
                <th style="color: #b10c0c;">Departamento </th>
                <th style="color: #b10c0c;">Denominacion Programa</th>
            </tr>
HTML

foreach my $resultado (@resultados) {
    print "<tr>";
    print "<td >$resultado->{'NOMBRE'}</td>";
    print "<td >$resultado->{'PERIODO_LICENCIAMIENTO'}</td>";
    print "<td >$resultado->{'DEPARTAMENTO_LOCAL'}</td>";
    print "<td >$resultado->{'DENOMINACION_PROGRAMA'}</td>";
    print "</tr>";
}
