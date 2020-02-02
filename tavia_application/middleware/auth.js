const jwt = require("jsonwebtoken");
const config = require("config");

// As this is middleware we need to export a mmiddleware function which takes in the three parameters
// A middleware function is basically a function that has access to the req and res cycle. next is a
// callback so that it moves onto the next piece of middleware once we are done
module.exports = function(req, res, next) {
  // Get token from header
  const token = req.header("x-auth-token");

  // Check if no token
  if (!token) {
    return res.status(401).json({ msg: "No token, authorisation denied" });
  }

  // Verify the token
  try {
    const decoded = jwt.verify(token, config.get("jwtSecret"));
    req.user = decoded.user;
    next();
  } catch (err) {
    res.status(401).json({ msg: "Token is not valid" });
  }
};
