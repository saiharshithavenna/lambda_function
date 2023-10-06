exports.handler = async (event, context) => {
    try {
      
      const message = "Hello, World!";
  
      
      return {
        statusCode: 200,
        body: JSON.stringify({ message }),
      };
    } catch (error) {
      // Handle errors
      return {
        statusCode: 500,
        body: JSON.stringify({ error: "Internal Server Error" }),
      };
    }
  };
  