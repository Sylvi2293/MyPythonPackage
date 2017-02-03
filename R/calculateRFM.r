#' calculateRFM
#'
# Description
#'	Calculate the a weighted RMF score: recency, frequency, and monetary for every customers
#
# Arguments
#'@param	data - A data.table containing the transaction rececord details for every customer.
#'@param	r -  Weight of recency.
#'@param	f -  Weight of frequency.
#'@param	m -  Weight of monetary.
#'
#' @details
#' \code{data} contains the transactional data. The dataset must contain a
#'             column labeled "Customer" that allows unique customer identification
#'             and a column labeled "TransDate", indicating the purchase date.
#'             The column "PurchAmount" specifies the total spending per purchase.
#
# Return Value
#'@return	Returns a  data.data containing the recency, frequency and monetary
#'score as well as the weighted final score and the group membership.

calulateRFM <- function(data, weight_recency=1, weight_frequency=1, weight_monetary=1){

  # Make sure data is a data.table
  data <- data.table(data)

  # Ensure that the weights add up to one
  weight_recency2 <- weight_recency/sum(weight_recency, weight_frequency, weight_monetary)
  weight_frequency2 <- weight_frequency/sum(weight_recency, weight_frequency, weight_monetary)
  weight_monetary2 <- weight_monetary/sum(weight_recency, weight_frequency, weight_monetary)

  # RFM measures
  max.Date <- max(transactions$TransDate)
  temp <- data[,list(
    recency = as.numeric(max.Date - max(TransDate)),
    frequency = .N,
    monetary = sum(PurchAmount)/.N),
    by="Customer"
    ]

  # RFM scores
  temp <- temp[,list(Customer,
                     recency = as.numeric(cut2(-recency, g=3)),
                     frequency = as.numeric(cut2(frequency, g=3)),
                     monetary = as.numeric(cut2(monetary, g=3)))]

  # Overall RFM score
  temp[,finalscore:=weight_recency2*recency+weight_frequency2*frequency+weight_monetary2*monetary]

  # RFM group
  temp[,group:=round(finalscore)]

  # Return final table
  return(temp)
}
