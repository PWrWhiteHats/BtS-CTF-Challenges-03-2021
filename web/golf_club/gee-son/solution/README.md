## Solution

1. Get private key from webpage
2. Decode sessionid cookie, see it's signed JWT token (base 64 encoded)
3. Change user field to chad_admin in sessionid JWT token and sign it again with page private key. See, [solution.rb](./solution.rb)
4. Reload page, you should be logged as chad_admin
