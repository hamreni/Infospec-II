module Heap where

data Heap a 
    = E
    | T Int a (Heap a)  (Heap a)
    deriving (Eq, Show, Ord)

rank :: Heap a -> Int
rank E = 0
rank (T n _ _ _) = n 
