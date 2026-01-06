// 'use client';
// import React, { useContext, useState } from 'react';
// import { useRouter } from 'next/navigation';
// import { AuthContext } from "@/components/AuthContext";
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faEye, faEyeSlash, faEnvelope, faLock } from '@fortawesome/free-solid-svg-icons';
// import { faGoogle } from '@fortawesome/free-brands-svg-icons';
// import { toast, ToastContainer } from 'react-toastify';
// import 'react-toastify/dist/ReactToastify.css';

// const Login = () => {
//   const router = useRouter();
//   const { login } = useContext(AuthContext);

//   const [formData, setFormData] = useState({
//     email: '',
//     password: ''
//   });
//   const [showPassword, setShowPassword] = useState(false);
//   const [isLoading, setIsLoading] = useState(false);

//   const handleChange = (e) => {
//     const { name, value } = e.target;
//     setFormData(prev => ({
//       ...prev,
//       [name]: value
//     }));
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     setIsLoading(true);

//     try {
//       // Call the login function from AuthContext
//       await login(formData);
//       // Navigation is handled in AuthContext based on user role
//       // Admin users will be redirected to /admindashboard
//     } catch (error) {
//       toast.error(error.response?.data?.detail || 'Login failed. Please check your credentials.');
//       setIsLoading(false);
//     }
//   };

//   const handleForgetPassword = () => {
//     router.push("/forgetpassword");
//   };

//   const handleSignup = () => {
//     router.push("/signup");
//   };

//   return (
//     <div className="flex justify-center items-center min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 p-4">
//       <ToastContainer />
//       <div className="w-full max-w-md">
//         <div className="bg-white shadow-xl rounded-xl overflow-hidden">
//           {/* Header Section */}
//           <div className="bg-gradient-to-r from-blue-600 to-blue-500 p-6 text-center">
//             <h1 className="text-3xl font-bold text-white">Welcome Back</h1>
//             <p className="text-blue-100 mt-2">Sign in to access your account</p>
//           </div>
          
//           {/* Form Section */}
//           <div className="p-8">
//             <form onSubmit={handleSubmit} className="space-y-6">
//               {/* Email Field */}
//               <div className="space-y-2">
//                 <label className="block text-sm font-medium text-gray-700">Email Address</label>
//                 <div className="relative">
//                   <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
//                     <FontAwesomeIcon icon={faEnvelope} className="h-5 w-5 text-gray-400" />
//                   </div>
//                   <input
//                     type="email"
//                     name="email"
//                     value={formData.email}
//                     onChange={handleChange}
//                     placeholder="Enter your email"
//                     className="w-full pl-10 pr-3 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition text-black"
//                     required
//                   />
//                 </div>
//               </div>
              
//               {/* Password Field */}
//               <div className="space-y-2">
//                 <label className="block text-sm font-medium text-gray-700">Password</label>
//                 <div className="relative">
//                   <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
//                     <FontAwesomeIcon icon={faLock} className="h-5 w-5 text-gray-400" />
//                   </div>
//                   <input
//                     type={showPassword ? 'text' : 'password'}
//                     name="password"
//                     value={formData.password}
//                     onChange={handleChange}
//                     placeholder="Enter your password"
//                     className="w-full pl-10 pr-10 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition text-black"
//                     required
//                   />
//                   <button
//                     type="button"
//                     className="absolute inset-y-0 right-0 pr-3 flex items-center"
//                     onClick={() => setShowPassword(!showPassword)}
//                   >
//                     <FontAwesomeIcon 
//                       icon={showPassword ? faEyeSlash : faEye} 
//                       className="h-5 w-5 text-gray-500 hover:text-gray-700" 
//                     />
//                   </button>
//                 </div>
//               </div>

//               {/* Forgot Password Link */}
//               <div className="flex justify-end">
//                 <button
//                   type="button"
//                   onClick={handleForgetPassword}
//                   className="text-sm text-blue-600 hover:text-blue-800 transition-colors"
//                 >
//                   Forgot Password?
//                 </button>
//               </div>

//               {/* Submit Button */}
//               <button
//                 type="submit"
//                 disabled={isLoading}
//                 className={`
//                   w-full py-3 px-4 
//                   bg-blue-600 
//                   text-white 
//                   rounded-lg 
//                   font-medium
//                   transition-colors
//                   ${isLoading ? 'opacity-70 cursor-not-allowed' : 'hover:bg-blue-700'}
//                 `}
//               >
//                 {isLoading ? (
//                   <div className="flex items-center justify-center">
//                     <div className="w-5 h-5 border-t-2 border-white rounded-full animate-spin mr-2"></div>
//                     Signing in...
//                   </div>
//                 ) : (
//                   'Sign In'
//                 )}
//               </button>

//               {/* Divider */}
//               <div className="relative my-6">
//                 <div className="absolute inset-0 flex items-center">
//                   <div className="w-full border-t border-gray-300"></div>
//                 </div>
//                 <div className="relative flex justify-center text-sm">
//                   <span className="px-2 bg-white text-gray-500">Or continue with</span>
//                 </div>
//               </div>

//               {/* Social Login */}
//               <button
//                 type="button"
//                 className="w-full py-3 px-4 flex items-center justify-center space-x-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
//               >
//                 <FontAwesomeIcon icon={faGoogle} className="h-5 w-5 text-red-500" />
//                 <span>Sign in with Google</span>
//               </button>

//               {/* Sign Up Link */}
//               <div className="text-center mt-6">
//                 <p className="text-sm text-gray-600">
//                   Don't have an account?{' '}
//                   <button
//                     type="button"
//                     onClick={handleSignup}
//                     className="text-blue-600 hover:text-blue-800 font-medium transition-colors"
//                   >
//                     Sign up
//                   </button>
//                 </p>
//               </div>
//             </form>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default Login;



// 'use client';
// import React, { useContext, useState } from 'react';
// import { useRouter } from 'next/navigation';
// import { AuthContext } from "@/components/AuthContext";
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faEye, faEyeSlash, faEnvelope, faLock } from '@fortawesome/free-solid-svg-icons';
// import { faGoogle } from '@fortawesome/free-brands-svg-icons';
// import { toast, ToastContainer } from 'react-toastify';
// import 'react-toastify/dist/ReactToastify.css';

// const Login = () => {
//   const router = useRouter();
//   const { login } = useContext(AuthContext);

//   const [formData, setFormData] = useState({
//     email: '',
//     password: ''
//   });
//   const [showPassword, setShowPassword] = useState(false);
//   const [isLoading, setIsLoading] = useState(false);

//   const handleChange = (e) => {
//     const { name, value } = e.target;
//     setFormData(prev => ({
//       ...prev,
//       [name]: value
//     }));
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     setIsLoading(true);
  
//     const { success } = await login(formData);
//     setIsLoading(false);
    
//     if (!success) {
//       // The error toast is already shown by the login function
//       return;
//     }
    
//     // Success case is handled in AuthContext
//   };

//   const handleForgetPassword = () => {
//     router.push("/forgetpassword");
//   };

//   const handleSignup = () => {
//     router.push("/signup");
//   };

//   return (
//     <div className="flex justify-center items-center min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 p-4">
//       <ToastContainer />
//       <div className="w-full max-w-md">
//         <div className="bg-white shadow-xl rounded-xl overflow-hidden">
//           {/* Header Section */}
//           <div className="bg-gradient-to-r from-blue-600 to-blue-500 p-6 text-center">
//             <h1 className="text-3xl font-bold text-white">Welcome Back</h1>
//             <p className="text-blue-100 mt-2">Sign in to access your account</p>
//           </div>
          
//           {/* Form Section */}
//           <div className="p-8">
//             <form onSubmit={handleSubmit} className="space-y-6">
//               {/* Email Field */}
//               <div className="space-y-2">
//                 <label className="block text-sm font-medium text-gray-700">Email Address</label>
//                 <div className="relative">
//                   <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
//                     <FontAwesomeIcon icon={faEnvelope} className="h-5 w-5 text-gray-400" />
//                   </div>
//                   <input
//                     type="email"
//                     name="email"
//                     value={formData.email}
//                     onChange={handleChange}
//                     placeholder="Enter your email"
//                     className="w-full pl-10 pr-3 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition text-black"
//                     required
//                   />
//                 </div>
//               </div>
              
//               {/* Password Field */}
//               <div className="space-y-2">
//                 <label className="block text-sm font-medium text-gray-700">Password</label>
//                 <div className="relative">
//                   <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
//                     <FontAwesomeIcon icon={faLock} className="h-5 w-5 text-gray-400" />
//                   </div>
//                   <input
//                     type={showPassword ? 'text' : 'password'}
//                     name="password"
//                     value={formData.password}
//                     onChange={handleChange}
//                     placeholder="Enter your password"
//                     className="w-full pl-10 pr-10 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition text-black"
//                     required
//                   />
//                   <button
//                     type="button"
//                     className="absolute inset-y-0 right-0 pr-3 flex items-center"
//                     onClick={() => setShowPassword(!showPassword)}
//                   >
//                     <FontAwesomeIcon 
//                       icon={showPassword ? faEyeSlash : faEye} 
//                       className="h-5 w-5 text-gray-500 hover:text-gray-700" 
//                     />
//                   </button>
//                 </div>
//               </div>

//               {/* Forgot Password Link */}
//               <div className="flex justify-end">
//                 <button
//                   type="button"
//                   onClick={handleForgetPassword}
//                   className="text-sm text-blue-600 hover:text-blue-800 transition-colors"
//                 >
//                   Forgot Password?
//                 </button>
//               </div>

//               {/* Submit Button */}
//               <button
//                 type="submit"
//                 disabled={isLoading}
//                 className={`
//                   w-full py-3 px-4 
//                   bg-blue-600 
//                   text-white 
//                   rounded-lg 
//                   font-medium
//                   transition-colors
//                   ${isLoading ? 'opacity-70 cursor-not-allowed' : 'hover:bg-blue-700'}
//                 `}
//               >
//                 {isLoading ? (
//                   <div className="flex items-center justify-center">
//                     <div className="w-5 h-5 border-t-2 border-white rounded-full animate-spin mr-2"></div>
//                     Signing in...
//                   </div>
//                 ) : (
//                   'Sign In'
//                 )}
//               </button>

//               {/* Divider */}
//               <div className="relative my-6">
//                 <div className="absolute inset-0 flex items-center">
//                   <div className="w-full border-t border-gray-300"></div>
//                 </div>
//                 <div className="relative flex justify-center text-sm">
//                   <span className="px-2 bg-white text-gray-500">Or continue with</span>
//                 </div>
//               </div>

//               {/* Social Login */}
//               <button
//                 type="button"
//                 className="w-full py-3 px-4 flex items-center justify-center space-x-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
//               >
//                 <FontAwesomeIcon icon={faGoogle} className="h-5 w-5 text-red-500" />
//                 <span>Sign in with Google</span>
//               </button>

//               {/* Sign Up Link */}
//               <div className="text-center mt-6">
//                 <p className="text-sm text-gray-600">
//                   Don't have an account?{' '}
//                   <button
//                     type="button"
//                     onClick={handleSignup}
//                     className="text-blue-600 hover:text-blue-800 font-medium transition-colors"
//                   >
//                     Sign up
//                   </button>
//                 </p>
//               </div>
//             </form>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default Login;






'use client';
import { useContext, useState, useEffect } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { AuthContext } from '@/components/AuthContext';
import AxiosInstance from '@/components/AxiosInstance';
// import GoogleLoginButton from '@/components/GoogleLoginButton';

const Login = () => {
  const { login } = useContext(AuthContext);
  const router = useRouter();
  const searchParams = useSearchParams();
  
  const [formData, setFormData] = useState({
    email: '',  // Changed from 'username' to 'email' to match backend
    password: ''
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);
  const [rememberMe, setRememberMe] = useState(false);

  // Check for registration success message
  useEffect(() => {
    if (searchParams.get('registered') === 'true') {
      setSuccess('Registration successful! Please login to continue.');
      // Clear the URL parameter after showing the message
      setTimeout(() => {
        setSuccess('');
        router.replace('/login');
      }, 5000);
    }
  }, [searchParams, router]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // Clear messages when user starts typing
    if (error) setError('');
    if (success) setSuccess('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    setLoading(true);

    // Basic validation
    if (!formData.email || !formData.password) {
      setError('Please enter both email and password');
      setLoading(false);
      return;
    }

    // Email format validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.email)) {
      setError('Please enter a valid email address');
      setLoading(false);
      return;
    }

    try {
      console.log('Attempting login with:', { email: formData.email });
      
      // Call your login API - backend expects { email, password }
      const response = await AxiosInstance.post('users/login', formData);
      
      console.log('Login API response:', response.data);

      // FastAPI backend returns: { message: "Login successful", access_token: "...", ... }
      if (response.data.message === 'Login successful' && response.data.access_token) {
        // Pass response.data directly to login function
        login(response.data);
        
        // Handle remember me functionality
        if (rememberMe && typeof window !== 'undefined') {
          localStorage.setItem('rememberMe', 'true');
          localStorage.setItem('lastEmail', formData.email);
        }
        
        // Notify the sidebar about auth change
        if (typeof window !== 'undefined') {
          window.dispatchEvent(new Event('authStateChanged'));
        }
        
        console.log('Login successful, redirecting to admindashboard...');
        router.push('/admindashboard');

      } else {
        setError(response.data.message || 'Login failed. Please try again.');
      }
    } catch (err) {
      console.error('Login error:', err);
      
      // Handle different error scenarios
      if (err.response) {
        // Server responded with error status
        const errorMessage = err.response.data?.message 
          || err.response.data?.detail 
          || err.response.data?.error
          || 'Invalid credentials. Please try again.';
        
        // Provide user-friendly messages for common errors
        if (err.response.status === 401) {
          setError('Invalid email or password. Please try again.');
        } else if (err.response.status === 404) {
          setError('Account not found. Please check your email or sign up.');
        } else if (err.response.status === 403) {
          setError('Account is inactive. Please contact support.');
        } else if (err.response.status === 422) {
          setError('Invalid input format. Please check your email and password.');
        } else {
          setError(errorMessage);
        }
      } else if (err.request) {
        // Request was made but no response received
        setError('Unable to connect to server. Please check your connection.');
      } else {
        // Something else happened
        setError('An unexpected error occurred. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  // Load remembered email on mount
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const remembered = localStorage.getItem('rememberMe') === 'true';
      const lastEmail = localStorage.getItem('lastEmail');
      
      if (remembered && lastEmail) {
        setFormData(prev => ({ ...prev, email: lastEmail }));
        setRememberMe(true);
      }
    }
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Animated background elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -inset-10 opacity-20">
          <div className="absolute top-1/4 left-1/4 w-72 h-72 bg-gradient-to-r from-amber-400 to-orange-500 rounded-full blur-3xl animate-pulse"></div>
          <div className="absolute bottom-1/4 right-1/4 w-72 h-72 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full blur-3xl animate-pulse delay-1000"></div>
        </div>
      </div>

      <div className="relative bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl shadow-2xl w-full max-w-md mx-4 overflow-hidden">
        {/* Decorative header */}
        <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-amber-400 via-rose-500 to-cyan-400"></div>
        
        <div className="p-8">
          {/* Logo/Brand */}
          <div className="text-center mb-8">
            <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-amber-400 to-orange-500 rounded-2xl shadow-lg mb-4">
              <span className="text-2xl font-bold text-white">L</span>
            </div>
            <h2 className="text-3xl font-light text-white tracking-wide">
              Welcome Back
            </h2>
            <p className="text-white/60 text-sm mt-2 font-light">
              Sign in to your account
            </p>
          </div>
          
          {/* Success Message */}
          {success && (
            <div className="mb-6 p-4 bg-emerald-500/20 border border-emerald-500/30 text-white rounded-xl backdrop-blur-sm animate-fade-in">
              <div className="flex items-center">
                <svg className="w-5 h-5 mr-2 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                <span className="text-sm">{success}</span>
              </div>
            </div>
          )}

          {/* Error Message */}
          {error && (
            <div className="mb-6 p-4 bg-rose-500/20 border border-rose-500/30 text-white rounded-xl backdrop-blur-sm animate-shake">
              <div className="flex items-center">
                <svg className="w-5 h-5 mr-2 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                </svg>
                <span className="text-sm">{error}</span>
              </div>
            </div>
          )}
          
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Email Field */}
            <div className="group">
              <label 
                htmlFor="email" 
                className="block text-sm font-medium text-white/80 mb-2 transition-all duration-300 group-focus-within:text-amber-300"
              >
                Email Address
              </label>
              <div className="relative">
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder-white/40 focus:outline-none focus:ring-2 focus:ring-amber-400/50 focus:border-amber-400/30 transition-all duration-300 backdrop-blur-sm"
                  placeholder="Enter your email"
                  required
                  disabled={loading}
                  autoComplete="email"
                />
                <div className="absolute right-3 top-1/2 transform -translate-y-1/2 text-white/40">
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                  </svg>
                </div>
              </div>
            </div>
            
            {/* Password Field */}
            <div className="group">
              <label 
                htmlFor="password" 
                className="block text-sm font-medium text-white/80 mb-2 transition-all duration-300 group-focus-within:text-cyan-300"
              >
                Password
              </label>
              <div className="relative">
                <input
                  type="password"
                  id="password"
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder-white/40 focus:outline-none focus:ring-2 focus:ring-cyan-400/50 focus:border-cyan-400/30 transition-all duration-300 backdrop-blur-sm"
                  placeholder="Enter your password"
                  required
                  disabled={loading}
                  autoComplete="current-password"
                />
                <div className="absolute right-3 top-1/2 transform -translate-y-1/2 text-white/40">
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
              </div>
            </div>
            
            {/* Remember Me & Forgot Password */}
            <div className="flex items-center justify-between">
              <label className="flex items-center text-white/70 text-sm cursor-pointer group">
                <input 
                  type="checkbox" 
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                  className="rounded bg-white/10 border-white/20 text-amber-400 focus:ring-amber-400/50 cursor-pointer transition-all duration-300" 
                />
                <span className="ml-2 group-hover:text-white/90 transition-colors duration-300">Remember me</span>
              </label>
              <a 
                href="/forgetpassword" 
                className="text-sm text-cyan-300 hover:text-cyan-200 transition-colors duration-300 hover:underline"
              >
                Forgot password?
              </a>
            </div>
            
            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className={`w-full py-4 px-6 rounded-xl font-medium text-white transition-all duration-300 transform hover:scale-[1.02] active:scale-[0.98] ${
                loading 
                  ? 'bg-gray-500 cursor-not-allowed' 
                  : 'bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 shadow-lg hover:shadow-amber-500/25'
              }`}
            >
              {loading ? (
                <span className="flex items-center justify-center">
                  <svg className="animate-spin h-5 w-5 mr-3" viewBox="0 0 24 24">
                    <circle 
                      className="opacity-25" 
                      cx="12" 
                      cy="12" 
                      r="10" 
                      stroke="currentColor" 
                      strokeWidth="4"
                      fill="none"
                    />
                    <path 
                      className="opacity-75" 
                      fill="currentColor" 
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    />
                  </svg>
                  Signing in...
                </span>
              ) : (
                <span className="flex items-center justify-center">
                  Sign In
                  <svg className="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </span>
              )}
            </button>
          </form>
          
          {/* Divider */}
          <div className="relative my-8">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-white/10"></div>
            </div>
            <div className="relative flex justify-center text-sm">
              <span className="px-2 text-white/40 bg-transparent">Or continue with</span>
            </div>
          </div>
          
          {/* Google Login Button */}
          <div className="mb-6">
            {/* <GoogleLoginButton /> */}
          </div>
          
          {/* Sign Up Link */}
          <div className="text-center">
            <span className="text-white/60 text-sm">
              Don't have an account?{' '}
            </span>
            <a 
              href="/signup" 
              className="text-sm text-cyan-300 hover:text-cyan-200 transition-colors duration-300 font-medium hover:underline"
            >
              Create account
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;