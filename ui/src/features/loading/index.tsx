import React, { FC } from 'react';
import ReactDOM from 'react-dom';

interface LoadingPropTypes {
  status?: string;
  loading: boolean;
}

const Loading = ({ status, loading }: LoadingPropTypes) => {
  const loadingComponent = loading ? (
    <div className="h-screen w-screen backdrop-blur-sm absolute top-0 left-0 flex justify-center items-center">
      <div className="w-[142px] h-[40px] contrast-[20]">
        {status && (
          <p className="text-2xl md:text-3xl mb-[10px] text-center">{status}</p>
        )}
        <span className="absolute w-[18px] h-[18px] left-[15px] bg-white rounded-full translate-x-0 animate-loading-dot" />
        <div className="translate-x-0 ml-[31px]">
          <span className="block w-[18px] h-[18px] ml-[18px] bg-black rounded-full float-left animate-loading-dots animate-delay-200" />
          <span className="block w-[18px] h-[18px] ml-[18px] bg-black rounded-full float-left animate-loading-dots animate-delay-600" />
          <span className="block w-[18px] h-[18px] ml-[18px] bg-black rounded-full float-left animate-loading-dots animate-delay-1100" />
        </div>
      </div>
    </div>
  ) : null;

  return ReactDOM.createPortal(
    loadingComponent,
    document.querySelector('#loading') as Element
  );
};

export default Loading;
