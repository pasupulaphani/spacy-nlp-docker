const zerorpc = require("zerorpc");

const client = new zerorpc.Client();

const port = process.env.ZEROMQ_PORT || "4242";
const host = process.env.ZEROMQ_HOST || "0.0.0.0";

console.log(`Connecting to tcp://${host}:${port}`)
client.connect(`tcp://${host}:${port}`);

client.on("error", function(error) {
  console.error("RPC client error:", error);
});

client.invoke("parse", "hotel new york", function(error, res, more) {
  if(error) {
    console.error(error);
  } else {
    console.log("Replied:", res);
  }

  if(!more) {
    console.log("Done.");
  }
});

client.invoke("nounChunks", "hotel new york", function(error, res, more) {
  if(error) {
    console.error(error);
  } else {
    console.log("Replied:", res);
  }

  if(!more) {
    console.log("Done.");
  }
});
