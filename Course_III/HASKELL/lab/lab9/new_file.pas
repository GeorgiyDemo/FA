const 
  SzM = 10; 
  SzN = 10; 
type Matrix = array [1..SzM,1..SzN] of integer;
procedure FillMatrixByRandom(var a: Matrix; m,n: integer);
begin
  for var i:=1 to M do 
  for var j:=1 to N do 
    a[i,j] := Random(10);
end;
procedure PrintMatrix(const a: Matrix; m,n: integer);
begin
  for var i:=1 to M do 
  begin
    for var j:=1 to N do 
      write(a[i,j]:4);
    writeln;  
  end;
end;
var a: Matrix;
begin
  var m := 4;
  var n := 5;
  FillMatrixByRandom(a,m,n);
  writeln('\208\173\208\187\208\181\208\188\208\181\208\189\209\130\209\139 \208\188\208\176\209\130\209\128\208\184\209\134\209\139: ');
  PrintMatrix(a,m,n);
end.


