data LTree = Unit Char Bool [LTree] deriving (Eq,Show)
 
tree2list :: LTree -> String -> [String]
tree2list (Unit c True _) acc = [acc ++ [c]] 
tree2list (Unit c False ts) acc = concatMap (\ u -> tree2list u (acc++[c])) ts
 
exist :: LTree -> String -> Bool
exist t s = s `elem` (tree2list t "") 
 
completions :: LTree -> String -> [String]
completions t s = filter (\ u -> s == take n u) tt
                  where n  = length s
                        tt = tree2list t ""
 
main = do 

    print(exist (Unit 'b' False [(Unit 'u' False [(Unit 'm' True []),(Unit 'x' True [])])]) "bum")
    print(exist (Unit 'b' False [(Unit 'u' False [(Unit 'm' True []),(Unit 'x' True [])])]) "bam")          
    print(completions (Unit 'b' False [(Unit 'u' False [(Unit 'm' True []),(Unit 'x' True [])])]) "bu")
    print(completions (Unit 'b' False [(Unit 'u' False [(Unit 'm' True []),(Unit 'x' True [])])]) "ba")