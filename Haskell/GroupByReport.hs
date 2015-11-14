import Data.List.Split
main = do
    context <- readFile("SalesDB.slc")
    let salesDB = lines context
    context <- readFile("SalesDB.slc")
    let salesDBCopy = lines context
    groupReport (salesDB,salesDBCopy,[])




groupReport :: ([String],[String],[Int]) -> IO()
groupReport ([],salesDBCopy,custList) = return()
groupReport ((salesRecord:salesDB),salesDBCopy,custList) =
            do
              let custId = read (splitFunction(salesRecord)!!1) :: Int
              if (elem custId custList) == False then
                do
                  getSalesDBCopy(salesRecord,salesDBCopy,0.0)
                  groupReport(salesDB,salesDBCopy,(custId : custList))
              else
                  groupReport(salesDB,salesDBCopy,custList)



getSalesDBCopy :: (String,[String],Float) -> IO()
getSalesDBCopy (salesRecord,[],total) =
                do
                   putStrLn $ splitFunction(salesRecord)!!1 ++ "  " ++ show (total)
getSalesDBCopy (salesRecord,(salesDBCopyRecord:salesDBCopy),total) =
                do
                  if (read (splitFunction(salesRecord)!!1) :: Int) == (read (splitFunction(salesDBCopyRecord)!!1) :: Int) then
                      getSalesDBCopy(salesRecord,salesDBCopy,(total + (read (splitFunction(salesDBCopyRecord)!!3) :: Float)))
                  else
                      getSalesDBCopy(salesRecord,salesDBCopy,total)
splitFunction :: String -> [String]
splitFunction record = splitOn "|" record
