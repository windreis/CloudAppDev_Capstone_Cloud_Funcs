/**
 * Get dealerships
 */

 const Cloudant = require('@cloudant/cloudant');

 async function main(params) {
     const cloudant = Cloudant({
         url: params.COUCH_URL,
         plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } }
     });

     let selector = {};
     if (params.state) {
         selector.st = { '$eq': params.state };
     }
     
     try {
         const dbListPromise = await getDbs(cloudant, selector);
         let tot_records = dbListPromise["dealerships"].length;
         if (tot_records > 0){
             return dbListPromise;
         }else{
             if (params.state){
                 return {
                     "status": 404,
                     "message": "The state does not exist"
                 };
             }else{
                return {
                     "status": 404,
                     "message": "The database is empty"
                };
             }
         }
     }
     catch{
         return {
            "status": 500,
            "error": "Something went wrong on the server"
        };
     }
 }

 function getDbs(cloudant, selector={}) {
     return new Promise((resolve, reject) => {
         const db = cloudant.use('dealerships');
         db.find({ selector, use_index: '_design/st' })
         .then(result => {
             resolve({ dealerships: formatData(result) })
         })
         .catch(err => {
             reject({ err: err});
         });
     });
 }

 function formatData(result) {
     return result.docs.map((row) => {
         const doc = row;
         return {
             "id": doc._id,
             "city": doc.city,
             "state": doc.state,
             "st": doc.st,
             "address": doc.address,
             "zip": doc.zip,
             "lat": doc.lat,
             "long": doc.long
         }
     })
 }