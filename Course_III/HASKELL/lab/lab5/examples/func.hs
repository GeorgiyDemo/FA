--class Functor f where
--fmap :: (a -> b) -> f a -> f b

data T1 =  A|B	-- перечислениe
{-
instance Functor T1 where
	fmap f A = 1
	fmap f B = 2
-}	
data BinaryTree a =
	EmptyBinaryTree
	| Leaf a
	| Node a (BinaryTree a) (BinaryTree a)
instance Functor BinaryTree where
	fmap f (EmptyBinaryTree) = EmptyBinaryTree
	fmap f (Leaf x) = Leaf (f x)
	fmap f (Node e l r) =
		Node (f e) (fmap f l) (fmap f r)

--xx::BinaryTree
x1 = Leaf 2
x2 = Leaf 3
xx = Node 4 x1 x2

