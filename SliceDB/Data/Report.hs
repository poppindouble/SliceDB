import Data.List.Split
main = do
    context <- readFile("CustDB.slc")
    let custDB = lines context
    context <- readFile("SalesDB.slc")
    let salesDB = lines context
    context <- readFile("OrderDB.slc")
    let orderDB = lines context
    finalResult(custDB,salesDB,orderDB)



finalResult :: ([String],[String],[String]) -> IO()
finalResult ([],salesDB,orderDB) = return()
finalResult ((custRecord:custDB),salesDB,orderDB) =
            do
              getCustDB(salesDB,orderDB,custRecord)
              finalResult(custDB,salesDB,orderDB)




getCustDB :: ([String],[String],String) -> IO()
getCustDB (salesDB,orderDB,custRecord) =
          do
            let ageLine = 60
            if(read (splitFunction(custRecord)!!2) :: Int) >= ageLine then
              getSalesDB(custRecord,salesDB,orderDB)
            else
              return ()


getSalesDB :: (String,[String],[String]) -> IO()
getSalesDB (custRecord,[],orderDB) = return()
getSalesDB (custRecord,(salesRecord:salesDB),orderDB) =
          do
            getOrderDB(custRecord,salesRecord,orderDB)
            getSalesDB(custRecord,salesDB,orderDB)

getOrderDB :: (String,String,[String]) -> IO()
getOrderDB (custRecord,salesRecord,orderDB) =
          do
            if ((read (splitFunction(custRecord)!!0) :: Int) == (read (splitFunction(salesRecord)!!1) :: Int)) then
              print (splitFunction(custRecord)!!1 ++ "|" ++ splitFunction(salesRecord)!!0 ++ "|" ++ splitFunction(salesRecord)!!2 ++ "|" ++ init (getItems((splitFunction(salesRecord)!!0),"",orderDB)))
            else
              return()


getItems :: (String,String,[String]) -> String
getItems (order,items,[]) = items
getItems (order,items,(x:xs))
        | (read order :: Int) == (read (splitFunction(x)!!0) :: Int) = getItems(order,(items ++ splitFunction(x)!!1 ++ ","),xs)
        | otherwise = getItems(order,items,xs)


splitFunction :: String -> [String]
splitFunction record = splitOn "|" record
