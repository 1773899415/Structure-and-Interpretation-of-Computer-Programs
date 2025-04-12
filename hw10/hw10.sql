.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name,size FROM dogs,sizes WHERE height>min AND height <=max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child AS name FROM parents,dogs WHERE parent=name ORDER BY height DESC;

--这个对每个column的名字也有要求我真是醉了 得AS name

-- Sentences about siblings that are the same size
CREATE TABLE mysiblings AS
  SELECT a.child AS CHILD1,b.child AS CHILD2 FROM parents AS a,parents AS b WHERE a.parent=b.parent AND a.child<b.child;
CREATE TABLE pair AS
  SELECT CHILD1,CHILD2,a.height AS HEIGHT1,b.height AS HEIGHT2 FROM mysiblings,dogs AS a,dogs AS b
  WHERE CHILD1=a.name AND CHILD2=b.name;
CREATE TABLE sentences AS
  SELECT "The two siblings, "||CHILD1||" plus "||CHILD2||" have the same size: "||size
  FROM pair,sizes WHERE HEIGHT1>min AND HEIGHT1<=max AND HEIGHT2>MIN AND HEIGHT2<=max;
