export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Example Route: /services/digital-marketing-port-harcourt-oil-gas
    // Matches: /services/:service-:location-:industry
    if (path.startsWith('/services/')) {
      const slug = path.replace('/services/', '');
      const parts = slug.split('-');

      // Fallback response or dynamic rendering
      if (parts.length >= 3) {
        const service = parts[0].replace(/-/g, ' ');
        const location = parts[1].replace(/-/g, ' ');
        const industry = parts.slice(2).join(' ');

        // Return dynamically generated HTML at the edge
        return new Response(`
          <!DOCTYPE html>
          <html lang="en">
          <head>
            <title>${service} in ${location} for ${industry} - TIDA</title>
            <meta name="description" content="Top-tier ${service} services in ${location} tailored for the ${industry} sector.">
          </head>
          <body>
            <h1>${service} in ${location}</h1>
            <p>Specialized ${service} solutions for the ${industry} industry in ${location}.</p>
          </body>
          </html>
        `, {
          headers: { 'Content-Type': 'text/html;charset=UTF-8' }
        });
      }
    }

    // Default response for unhandled routes
    return fetch(request);
  }
};