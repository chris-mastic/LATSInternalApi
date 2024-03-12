const beginTaxYear  = 1960;

const endTaxYear = (new Date().getFullYear()) + 1;

const getTaxYears = ()=> {

  const options = []

  for (let i = endTaxYear; i >= beginTaxYear; i-- ){
    options.push({value : i , label : `${i}`})
  }

  return options;
}

export const taxyearOptions = getTaxYears();